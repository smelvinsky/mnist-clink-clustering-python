`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 31.05.2018 20:39:54
// Design Name: 
// Module Name: distance
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

module distance( clock, reset, start, image1_in_0, image1_in_1, image1_in_2, image1_in_3, image1_in_4, image1_in_5, image1_in_6, 
image1_in_7, image1_in_8, image1_in_9, image1_in_10, image1_in_11, image1_in_12, image1_in_13, image1_in_14, image1_in_15, 
image1_in_16, image1_in_17, image1_in_18, image1_in_19, image1_in_20, image1_in_21, image1_in_22, image1_in_23, image1_in_24, 
image1_in_25, image1_in_26, image1_in_27, image2_in_0, image2_in_1, image2_in_2, image2_in_3, image2_in_4, image2_in_5, image2_in_6, 
image2_in_7, image2_in_8, image2_in_9, image2_in_10, image2_in_11, image2_in_12, image2_in_13, image2_in_14, image2_in_15, image2_in_16, 
image2_in_17, image2_in_18, image2_in_19, image2_in_20, image2_in_21, image2_in_22, image2_in_23, image2_in_24, image2_in_25, image2_in_26, 
image2_in_27, ready_out, distance_out);
parameter integer n = 28; 
input clock, reset;
input start; //start processing
input [27:0] image1_in_0, image1_in_1, image1_in_2, image1_in_3, image1_in_4, image1_in_5, image1_in_6, 
image1_in_7, image1_in_8, image1_in_9, image1_in_10, image1_in_11, image1_in_12, image1_in_13, image1_in_14, image1_in_15, 
image1_in_16, image1_in_17, image1_in_18, image1_in_19, image1_in_20, image1_in_21, image1_in_22, image1_in_23, image1_in_24, 
image1_in_25, image1_in_26, image1_in_27, image2_in_0, image2_in_1, image2_in_2, image2_in_3, image2_in_4, image2_in_5, image2_in_6, 
image2_in_7, image2_in_8, image2_in_9, image2_in_10, image2_in_11, image2_in_12, image2_in_13, image2_in_14, image2_in_15, image2_in_16, 
image2_in_17, image2_in_18, image2_in_19, image2_in_20, image2_in_21, image2_in_22, image2_in_23, image2_in_24, image2_in_25, image2_in_26, 
image2_in_27;  
output reg ready_out; //result is ready
output reg [27:0] distance_out;
//FSMD states
parameter S1 = 4'h01, S2 = 4'h02, S3 = 4'h03, S4 = 4'h04, S5 = 4'h05, S6 = 4'h06, S7 = 4'h07;
reg [3:0] state;
////Algorithm Variables
wire [27:0] image1_in[0:27];
wire [27:0] image2_in[0:27];
reg [27:0] xor_result[0:27];
assign image1_in[0] = image1_in_0;
assign image1_in[1] = image1_in_1;
assign image1_in[2] = image1_in_2;
assign image1_in[3] = image1_in_3;
assign image1_in[4] = image1_in_4;
assign image1_in[5] = image1_in_5;
assign image1_in[6] = image1_in_6;
assign image1_in[7] = image1_in_7;
assign image1_in[8] = image1_in_8;
assign image1_in[9] = image1_in_9;
assign image1_in[10] = image1_in_10;
assign image1_in[11] = image1_in_11;
assign image1_in[12] = image1_in_12;
assign image1_in[13] = image1_in_13;
assign image1_in[14] = image1_in_14;
assign image1_in[15] = image1_in_15;
assign image1_in[16] = image1_in_16;
assign image1_in[17] = image1_in_17;
assign image1_in[18] = image1_in_18;
assign image1_in[19] = image1_in_19;
assign image1_in[20] = image1_in_20;
assign image1_in[21] = image1_in_21;
assign image1_in[22] = image1_in_22;
assign image1_in[23] = image1_in_23;
assign image1_in[24] = image1_in_24;
assign image1_in[25] = image1_in_25;
assign image1_in[26] = image1_in_26;
assign image1_in[27] = image1_in_27;
assign image2_in[0] = image2_in_0;
assign image2_in[1] = image2_in_1;
assign image2_in[2] = image2_in_2;
assign image2_in[3] = image2_in_3;
assign image2_in[4] = image2_in_4;
assign image2_in[5] = image2_in_5;
assign image2_in[6] = image2_in_6;
assign image2_in[7] = image2_in_7;
assign image2_in[8] = image2_in_8;
assign image2_in[9] = image2_in_9;
assign image2_in[10] = image2_in_10;
assign image2_in[11] = image2_in_11;
assign image2_in[12] = image2_in_12;
assign image2_in[13] = image2_in_13;
assign image2_in[14] = image2_in_14;
assign image2_in[15] = image2_in_15;
assign image2_in[16] = image2_in_16;
assign image2_in[17] = image2_in_17;
assign image2_in[18] = image2_in_18;
assign image2_in[19] = image2_in_19;
assign image2_in[20] = image2_in_20;
assign image2_in[21] = image2_in_21;
assign image2_in[22] = image2_in_22;
assign image2_in[23] = image2_in_23;
assign image2_in[24] = image2_in_24;
assign image2_in[25] = image2_in_25;
assign image2_in[26] = image2_in_26;
assign image2_in[27] = image2_in_27;

////Iterators
reg [4:0] i, j, k, line_number;

always @ (posedge clock)
    begin

    if(reset==1'b1)
        begin
        ready_out <= 1'b0;
        state <= S1;
    end
    else
        begin
        case(state)
            S1: begin
                if(start == 1'b1) state <= S2; else state <= S1;
            end

            S2: begin
                distance_out <= 0;
                ready_out <= 0;
                i <= 0;
                j <= 0;
                k <=0;
                line_number <= 0;
                state <= S3;
            end

            S3: begin
                for (i=0; i<n; i=i+1)
                xor_result[i] <= 0;
                state <= S4;
            end

            S4: begin
                for (line_number = 0; line_number<n; line_number = line_number+1)
                    for (j = 0; j<n; j=j+1)
                        xor_result[line_number] = xor_result[line_number] + image1_in[line_number][j]^image2_in[line_number][j];
                state <= S5;    
            end

            S5:begin
                for(k=0; k<n; k=k+1)
                    distance_out = distance_out + xor_result[k];
                state <= S6;
                end

            S6:begin
                ready_out = 1;
                state <= S7;
            end

            S7:begin
                if(start == 1'b0) state <= S1; else state <= S7;
            end

        endcase
    end
end
endmodule