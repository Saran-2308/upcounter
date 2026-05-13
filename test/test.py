import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_upcounter(dut):

    cocotb.start_soon(Clock(dut.clk, 10, unit="us").start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # RESET (IMPORTANT FIX)
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)

    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # FIRST VALUE MUST BE 1
    val = int(dut.uo_out.value)
    assert val == 1, f"Expected 1, got {val}"

    # COUNT LOOP
    for i in range(2, 16):
        await ClockCycles(dut.clk, 1)
        val = int(dut.uo_out.value) & 0xF
        assert val == i, f"Expected {i}, got {val}"

    # OVERFLOW
    await ClockCycles(dut.clk, 1)
    assert (int(dut.uo_out.value) & 0xF) == 0
