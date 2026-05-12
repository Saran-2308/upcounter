## How it works

This project implements a **4-bit synchronous up counter** using Verilog.

The counter increments its value by 1 on every rising edge of the clock signal (`clk`).  
It uses an **active-low asynchronous reset (`rst_n`)**, which immediately resets the counter value to `0000` whenever reset is asserted low.

The 4-bit counter output is mapped to the dedicated output pins:

- `uo[0]` → Least Significant Bit (LSB)
- `uo[1]` → Counter bit 1
- `uo[2]` → Counter bit 2
- `uo[3]` → Most Significant Bit (MSB)

Counting sequence:

0000 → 0001 → 0010 → 0011 → 0100 → ... → 1111 → 0000

The counter continuously wraps around after reaching its maximum value (`1111`).

Unused input pins (`ui_in`) and bidirectional pins (`uio_in`) are ignored in this design.

---

## How to test

1. Apply power to the Tiny Tapeout chip.
2. Provide a clock signal to the `clk` input.
3. Set `rst_n = 0` to reset the counter.
4. Set `rst_n = 1` to release reset.
5. Observe the output pins `uo[3:0]`.

Expected behavior:

- After reset:
  `uo[3:0] = 0000`

- After first clock pulse:
  `uo[3:0] = 0001`

- After second clock pulse:
  `uo[3:0] = 0010`

- After third clock pulse:
  `uo[3:0] = 0011`

- ...

- After fifteenth clock pulse:
  `uo[3:0] = 1111`

- Next clock pulse:
  `uo[3:0] = 0000`

This behavior can also be verified using simulation with cocotb or GTKWave waveform viewer.

---

## External hardware

No external hardware is required.

Optional hardware for demonstration/testing:

- LED array (to visualize counter output)
- Clock generator
- Reset push button
- Logic analyzer / oscilloscope
