`timescale 1ns / 1ps
`default_nettype none

module BioEE_clkdivider(

	input wire clkin,
	input wire [31:0] integerdivider,  //even numbers only
	
	input wire enable,
	output reg clkout
	
   );


reg [30:0] clk_counter;

initial begin
	clk_counter <= 31'd00;
end

always @(posedge clkin) begin
	if ( (enable==1'b1) && (clk_counter == integerdivider[31:1]) ) begin
		clk_counter <= 31'd01;
		clkout <= ~clkout;
	end else begin
		clk_counter <= clk_counter + 1;
	end
end




endmodule

