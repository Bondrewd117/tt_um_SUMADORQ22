/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_SUMADORQ22 (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);
    assign uio_oe  = 8'b0000_0000;  // Set all IOs as inputs
    assign uio_out = 8'b0000_0000;  // Drive outputs to 0 when not used
    
    wire [4:0] a;
    wire [4:0] b;
    wire [5:0] c;

    assign a = ui_in[4:0];
    assign uo_out[5:0] = c;
    assign b = uio_in[4:0];
    assign uo_out[7:6] = 2'h0;

    SUMADORQ22 SUMADORQ22_Unit(
        .clk(clk),
        .rst(rst_n),
        .a(a), 
        .b(b),
        .c(c)
    );

    wire _unused = &{ena, uio_in[7:5], ui_in[7:5], 1'b0};
endmodule
