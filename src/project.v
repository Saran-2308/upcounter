`default_nettype none

module tt_um_upcounter (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    reg [3:0] count;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            count <= 0;
        else
            count <= count + 1'b1;
    end

    assign uo_out = {4'b0, count};
    assign uio_out = 0;
    assign uio_oe  = 0;

endmodule
