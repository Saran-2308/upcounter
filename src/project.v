/*
 * 4-bit Up Counter for Tiny Tapeout
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    
    output wire [7:0] uo_out,   
    input  wire [7:0] uio_in,   
    output wire [7:0] uio_out,  
    output wire [7:0] uio_oe,   
    input  wire       ena,      
    input  wire       clk,      
    input  wire       rst_n     
);

  reg [3:0] counter;

  // Up Counter Logic
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      counter <= 4'b0000;      // Reset counter
    else
      counter <= counter + 1;  // Increment
  end

  // Output counter value
  assign uo_out = {4'b0000, counter};

  // Unused IOs
  assign uio_out = 8'b00000000;
  assign uio_oe  = 8'b00000000;

  // Prevent warnings
  wire _unused = &{ena, ui_in, uio_in, 1'b0};

endmodule
