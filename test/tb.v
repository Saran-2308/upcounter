`default_nettype none
`timescale 1ns/1ps

module tb;

  initial begin
    $dumpfile("tb.vcd");
    $dumpvars(0, tb);
  end

  reg clk = 0;
  reg rst_n = 1;
  reg ena = 0;

  reg [7:0] ui_in = 0;
  reg [7:0] uio_in = 0;

  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;

  tt_um_upcounter dut (
      .ui_in(ui_in),
      .uo_out(uo_out),
      .uio_in(uio_in),
      .uio_out(uio_out),
      .uio_oe(uio_oe),
      .ena(ena),
      .clk(clk),
      .rst_n(rst_n)
  );

endmodule
