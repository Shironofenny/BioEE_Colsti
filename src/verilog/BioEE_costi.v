`timescale 1ns / 1ps

// ENDPOINT ADDRESS MAP  
// Endpoint Type	Address Range	Sync/Async	Data Type	 
// Wire In          0x00 - 0x1F	Asynchronous	Signal state	   
// Wire Out         0x20 - 0x3F	Asynchronous	Signal state	   
// Trigger In       0x40 - 0x5F	Synchronous	One-shot	   
// Trigger Out      0x60 - 0x7F	Synchronous	One-shot	   
// Pipe In          0x80 - 0x9F	Synchronous	Multi-byte transfer	   
// Pipe Out         0xA0 - 0xBF	Synchronous	Multi-byte transfer	 



`default_nettype none

module costi_bitfile(
   input  wire [7:0]  hi_in,
   output wire [1:0]  hi_out,
   inout  wire [15:0] hi_inout,
   
   output wire        i2c_sda,
   output wire        i2c_scl,
   output wire        hi_muxsel,
   
   input  wire        clk1,
   input  wire        clk2,
   output wire [7:0]  led,
   input  wire        button,

	inout  wire [57:0] xbus,
	inout  wire [57:0] ybus,

	output wire        sdram_cke,
	output wire        sdram_cs_n,
	output wire        sdram_we_n,
	output wire        sdram_cas_n,
	output wire        sdram_ras_n,
	output wire        sdram_ldqm,
	output wire        sdram_udqm,
	output wire [1:0]  sdram_ba,
	output wire [12:0] sdram_a,
	inout  wire [15:0] sdram_d
   	
   );


//========================================================================
// DUMMY PLACEHOLDER SIGNAL ASSIGNMENTS
//========================================================================

assign i2c_sda = 1'bz;
assign i2c_scl = 1'bz;
assign hi_muxsel = 1'b0;


//========================================================================
// CLOCKS
//========================================================================

wire global_reset;

wire clk1locked;

dcm_sys sdramDCM (
    .CLKIN_IN(clk1), 
    .RST_IN(global_reset), 
    .CLKIN_IBUFG_OUT(), 
    .CLK0_OUT(clk1locked),
    .LOCKED_OUT() );
	 
// This DCM seems to down count the clock into 100MHz

wire sdram_clk = clk1locked;
wire clk1out;
wire adc_clk;

BioEE_clkdivider clk1divider ( 	.clkin(clk1locked), 
											.integerdivider(31'd100000000), 
											.enable(1'b1),
											.clkout(clk1out) );

BioEE_clkdivider adcclkdivider ( .clkin(clk1locked), 
											.integerdivider(32'd100), 
											.enable(1'b1),
											.clkout(adc_clk) );


//========================================================================
// I/O Mapping
//========================================================================

wire [12:1] adc_data;
wire adc_otr;

OBUF OBUF_Y1 ( .I(adc_clk), .O(ybus[1]) );
IBUF IBUF_adcdata[12:1] ( .I( {ybus[3],ybus[5],ybus[7],ybus[9],ybus[11],ybus[13],ybus[15],ybus[17],ybus[19],ybus[21],ybus[23],ybus[25]} ), .O(adc_data[12:1]) );
IBUF IBUF_Y27 ( .I(ybus[27]), .O(adc_otr) );


//========================================================================
// OPAL KELLY INTERFACE SIGNAL DECLARATIONS
//========================================================================

wire         ti_clk;
wire [30:0]  ok1;
wire [16:0]  ok2;

wire [15:0]	bioee_triggerin_test1;
wire [15:0]	bioee_triggerout_test1;
wire [15:0] bioee_wirein_test1;
wire [15:0] bioee_wireout_test1;

wire [15:0] btpipeI_dac_data, btpipeO_adc_data, btpipeI_scanvector_data;
wire        btpipeI_dac_block, btpipeO_adc_block, btpipeI_scanvector_block;
wire        btpipeI_dac_write, btpipeO_adc_read, btpipeI_scanvector_write;
wire        btpipeI_dac_ready, btpipeO_adc_ready, btpipeI_scanvector_ready;


assign global_reset = bioee_wirein_test1[15];

//========================================================================
// OPAL KELLY INTERFACE INSTANTIATIONS
//========================================================================

okHostInterface okHI(
      .hi_in(hi_in), .hi_out(hi_out), .hi_inout(hi_inout),
		.ti_clk(ti_clk), .ok1(ok1), .ok2(ok2));

okTriggerIn ep40 (.ok1(ok1), .ok2(ok2), .ep_addr(8'h40), 
						.ep_clk(ti_clk), .ep_trigger(bioee_triggerin_test1));

okTriggerOut ep60 (.ok1(ok1), .ok2(ok2), .ep_addr(8'h60), 
						.ep_clk(ti_clk), .ep_trigger(bioee_triggerout_test1));

okWireIn ep00 (.ok1(ok1), .ok2(ok2), .ep_addr(8'h00), .ep_dataout(bioee_wirein_test1));

okWireOut ep20 (.ok1(ok1), .ok2(ok2), .ep_addr(8'h20), .ep_datain(bioee_wireout_test1));

okBTPipeIn ep80 (.ok1(ok1), .ok2(ok2),
	.ep_addr(8'h80), .ep_write(btpipeI_scanvector_write), 
	.ep_blockstrobe(btpipeI_scanvector_block), .ep_dataout(btpipeI_scanvector_data),
	.ep_ready(btpipeI_scanvector_ready));
	
okBTPipeOut epA0 (.ok1(ok1), .ok2(ok2),
	.ep_addr(8'ha0), .ep_read(btpipeO_adc_read), 
	.ep_blockstrobe(btpipeO_adc_block),  .ep_datain(btpipeO_adc_data),
	.ep_ready(btpipeO_adc_ready));



//========================================================================
// CONTROL VECTORS
//========================================================================

wire [15:0] scanvector_output;

BioEE_vector scanvector ( 	.vectorreset(global_reset), 
									.vectorclk(clk1out), 
									.ti_clk(ti_clk), 
									.btpipeI_vector_write(btpipeI_scanvector_write),
									.btpipeI_vector_block(btpipeI_scanvector_block),
									.btpipeI_vector_data(btpipeI_scanvector_data),
									.btpipeI_vector_ready(btpipeI_scanvector_ready),
									.vectoroutput(scanvector_output) );

wire chip_scan1clk = scanvector_output[0];
wire chip_scan1resetn = scanvector_output[1];
wire chip_scan1latch = scanvector_output[2];
wire chip_scan1data0 = scanvector_output[3];
wire chip_scan1data1 = scanvector_output[4];
wire chip_scan1data2 = scanvector_output[5];
wire chip_scan1data3 = scanvector_output[6];
wire chip_scan1data4 = scanvector_output[7];
wire chip_scan2clk = scanvector_output[8];
wire chip_scan2resetn = scanvector_output[9];
wire chip_scan2latch = scanvector_output[10];
wire chip_scan2data = scanvector_output[11];




//========================================================================
// ADC
//========================================================================

wire adc_fill_level_trigger;
assign bioee_triggerout_test1[0] = adc_fill_level_trigger;

BioEE_sdram_fifo adcfifo(
	.datain( { 3'b000, adc_otr, adc_data[1], adc_data[2], adc_data[3], adc_data[4], adc_data[5], adc_data[6], adc_data[7], adc_data[8], adc_data[9], adc_data[10], adc_data[11], adc_data[12] } ),
	.write_clk(adc_clk),
	.write_en(1'b1),
	
	.resetin(global_reset),
	
	.read_clk(ti_clk),
	.read_en(btpipeO_adc_read),
	.dataout(btpipeO_adc_data[15:0]),
	.read_ready(btpipeO_adc_ready),
	.fill_level_trigger(adc_fill_level_trigger),
	
	.sdram_clk(sdram_clk),
	.sdram_cke(sdram_cke),
	.sdram_cs_n(sdram_cs_n),
	.sdram_we_n(sdram_we_n),
	.sdram_cas_n(sdram_cas_n),
	.sdram_ras_n(sdram_ras_n),
	.sdram_ldqm(sdram_ldqm),
	.sdram_udqm(sdram_udqm),
	.sdram_ba(sdram_ba),
	.sdram_a(sdram_a),
	.sdram_d(sdram_d)
   
	// ---------------------------------
	);





//========================================================================
// LED indicators
//========================================================================


wire [7:0] led_signals = {		clk1out,
										chip_scan1clk,
										chip_scan1resetn,
										chip_scan1latch,
										chip_scan1data0,
										chip_scan1data1,
										bioee_wirein_test1[1],
										bioee_wirein_test1[0]};
										
OBUF OBUF_led[7:0] ( .I(~led_signals[7:0]), .O(led[7:0]) );

wire [57:0] xbus_test = 58'h3FFFFFFFFFFFFFF;
OBUF OBUF_xbus[57:0] ( .I(xbus_test[57:0]), .O(xbus[57:0]) );

	
endmodule




