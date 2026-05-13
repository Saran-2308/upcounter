`default_nettype none

module tt_um_upcounter (
    input  wire [7:0] ui_in,
    output reg  [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    reg [3:0] counter;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            counter <= 4'b0000;
        else if (ena)
            counter <= counter + 1'b1;
    end

    always @(*) begin
        uo_out = {4'b0000, counter};
    end

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

endmodule
