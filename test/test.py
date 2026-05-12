import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer


@cocotb.test()
async def test_upcounter(dut):
    dut._log.info("Starting Up Counter Test")

    # Start clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Initialize
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Apply reset
    dut.rst_n.value = 0
    await Timer(1, unit="us")   # allow reset to propagate

    # Check reset
    assert int(dut.uo_out.value) == 0, "Counter should be 0 after reset"

    # Release reset
    dut.rst_n.value = 1

    # Test counting
    for i in range(1, 16):
        await ClockCycles(dut.clk, 1)
        actual = int(dut.uo_out.value) & 0x0F
        expected = i

        dut._log.info(f"Expected={expected}, Actual={actual}")
        assert actual == expected, f"Expected {expected}, got {actual}"

    # Overflow test
    await ClockCycles(dut.clk, 1)
    assert (int(dut.uo_out.value) & 0x0F) == 0

    dut._log.info("Test Passed")
