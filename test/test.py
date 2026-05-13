import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_upcounter(dut):

    # Start clock
    cocotb.start_soon(Clock(dut.clk, 10, units="us").start())

    # Initial values
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset (active low)
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)

    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Check first increment
    assert int(dut.uo_out.value) == 1, f"Expected 1, got {dut.uo_out.value}"

    # Check counting 1 → 15
    for i in range(2, 16):
        await ClockCycles(dut.clk, 1)
        actual = int(dut.uo_out.value) & 0xF
        assert actual == i, f"Expected {i}, got {actual}"

    # Overflow check (15 → 0)
    await ClockCycles(dut.clk, 1)
    assert (int(dut.uo_out.value) & 0xF) == 0
