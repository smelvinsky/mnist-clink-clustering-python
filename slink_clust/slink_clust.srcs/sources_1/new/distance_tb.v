`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: AGH
// Engineer:  Rybicka M., Smela D.
// 
// Create Date: 30.05.2018 11:51:58
// Design Name: 
// Module Name: distance_tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module distance_tb;
reg clock, reset, start_in;
//reg [27:0] image1_in [0:27]; 
//reg [27:0] image2_in [0:27];  
wire ready_out;
wire [27:0] distance_out;
integer real_dist;
integer i=0;
reg [27:0] image1_in_0, image1_in_1, image1_in_2, image1_in_3, image1_in_4, image1_in_5, image1_in_6, 
                image1_in_7, image1_in_8, image1_in_9, image1_in_10, image1_in_11, image1_in_12, image1_in_13, image1_in_14, image1_in_15, 
                image1_in_16, image1_in_17, image1_in_18, image1_in_19, image1_in_20, image1_in_21, image1_in_22, image1_in_23, image1_in_24, 
                image1_in_25, image1_in_26, image1_in_27, image2_in_0, image2_in_1, image2_in_2, image2_in_3, image2_in_4, image2_in_5, image2_in_6, 
                image2_in_7, image2_in_8, image2_in_9, image2_in_10, image2_in_11, image2_in_12, image2_in_13, image2_in_14, image2_in_15, image2_in_16, 
                image2_in_17, image2_in_18, image2_in_19, image2_in_20, image2_in_21, image2_in_22, image2_in_23, image2_in_24, image2_in_25, image2_in_26, 
                image2_in_27;  
distance dist_tb( clock, reset, start_in, image1_in_0, image1_in_1, image1_in_2, image1_in_3, image1_in_4, image1_in_5, image1_in_6, 
                image1_in_7, image1_in_8, image1_in_9, image1_in_10, image1_in_11, image1_in_12, image1_in_13, image1_in_14, image1_in_15, 
                image1_in_16, image1_in_17, image1_in_18, image1_in_19, image1_in_20, image1_in_21, image1_in_22, image1_in_23, image1_in_24, 
                image1_in_25, image1_in_26, image1_in_27, image2_in_0, image2_in_1, image2_in_2, image2_in_3, image2_in_4, image2_in_5, image2_in_6, 
                image2_in_7, image2_in_8, image2_in_9, image2_in_10, image2_in_11, image2_in_12, image2_in_13, image2_in_14, image2_in_15, image2_in_16, 
                image2_in_17, image2_in_18, image2_in_19, image2_in_20, image2_in_21, image2_in_22, image2_in_23, image2_in_24, image2_in_25, image2_in_26, 
                image2_in_27, ready_out, distance_out);
//Clock generator
initial
    clock <= 1'b1;
always
    #5 clock <= ~clock;
//Reset signal
initial
begin
    reset <= 1'b1;
    #10 reset <= 1'b0;
end
//Stimuli signals
initial
begin
//   for (i=0; i<=27; i=i+1)
//   begin
        image1_in_0 = 28'hfffffff;
        image1_in_1 = 28'h0000000;
        image1_in_2 = 28'hfffffff;
        image1_in_3 = 28'hfffffff;
        image1_in_4 = 28'hfffffff;
        image1_in_5 = 28'hfffffff;
        image1_in_6 = 28'hfffffff;
        image1_in_7 = 28'hfffffff;
        image1_in_8 = 28'hfffffff;
        image1_in_9 = 28'hfffffff;
        image1_in_10 = 28'hfffffff;
        image1_in_11 = 28'hfffffff;
        image1_in_12 = 28'hfffffff;
        image1_in_13 = 28'hfffffff;
        image1_in_14 = 28'hfffffff;
        image1_in_15 = 28'hfffffff;
        image1_in_16 = 28'hfffffff;
        image1_in_17 = 28'hfffffff;
        image1_in_18 = 28'hfffffff;
        image1_in_19 = 28'hfffffff;
        image1_in_20 = 28'hfffffff;
        image1_in_21 = 28'hfffffff;
        image1_in_22 = 28'hfffffff;
        image1_in_23 = 28'hfffffff;
        image1_in_24 = 28'hfffffff;
        image1_in_25 = 28'hfffffff;
        image1_in_26 = 28'hfffffff;
        image1_in_27 = 28'hfffffff;
        image2_in_0 = 28'hfffffff;
        image2_in_1 = 0;
        image2_in_2 = 0;
        image2_in_3 = 0;
        image2_in_4 = 0;
        image2_in_5 = 0;
        image2_in_6 = 0;
        image2_in_7 = 0;
        image2_in_8 = 0;
        image2_in_9 = 0;
        image2_in_10 = 0;
        image2_in_11 = 0;
        image2_in_12 = 0;
        image2_in_13 = 0;
        image2_in_14 = 0;
        image2_in_15 = 0;
        image2_in_16 = 0;
        image2_in_17 = 0;
        image2_in_18 = 0;
        image2_in_19 = 0;
        image2_in_20 = 0;
        image2_in_21 = 0;
        image2_in_22 = 0;
        image2_in_23 = 0;
        image2_in_24 = 0;
        image2_in_25 = 0;
        image2_in_26 = 0;
        image2_in_27 = 0;
//   end
    start_in <= 1'b0;
    #20 start_in <= 1'b1;
    #30 start_in <= 1'b0;
end
//Catch output
always @ (posedge ready_out)
begin
    #200 real_dist = distance_out;
    $display("Distance calculated: distance=%d", real_dist);
end
endmodule
