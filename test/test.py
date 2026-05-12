# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_upcounter(dut):
    dut._log.info("Starting Up Counter Test")

    # Create 10 us clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Initialize signals
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Apply reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)

    # Check reset value
    assert dut.uo_out.value == 0, "Counter should be 0 after reset"

    # Release reset
    dut.rst_n.value = 1

    # Check counting sequence
    for i in range(1, 16):
        await ClockCycles(dut.clk, 1)
        expected = i & 0x0F   # 4-bit wraparound
        actual = int(dut.uo_out.value) & 0x0F

        dut._log.info(f"Expected: {expected}, Actual: {actual}")

        assert actual == expected, f"Counter mismatch! Expected {expected}, got {actual}"

    # Check overflow (1111 -> 0000)
    await ClockCycles(dut.clk, 1)
    assert (int(dut.uo_out.value) & 0x0F) == 0, "Counter should wrap to 0"

    dut._log.info("Up Counter Test Passed")
