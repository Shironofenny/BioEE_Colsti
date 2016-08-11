import imp
import sys

ok = imp.load_source('ok','../../lib/ok/ok.py')

xem = ok.okCFrontPanel()

pll = ok.PLL22393()

if (xem.NoError != xem.OpenBySerial("")):
    print("Error in opening FPGA")
    sys.exit()

xem.GetPLL22393Configuration(pll)
print(pll.GetPLLFrequency(0))
pll.SetReference(48.0)
pll.SetPLLParameters(0, 400, 48, True)
pll.SetOutputSource(0, ok.PLL22393.ClkSrc_PLL0_0)
pll.SetOutputDivider(0, 4)
pll.SetOutputEnable(0, True)
xem.SetPLL22393Configuration(pll)

output = xem.ConfigureFPGA('../FPGA/OKPythonSample.bit')
print(output)

output = xem.SetWireInValue(0x00,0x01)
output = xem.SetWireInValue(0x01,0x55)
print(output)

output = xem.UpdateWireIns()
print(output)

output = xem.ActivateTriggerIn(0x40,0x00)
print(output)

output = xem.SetWireInValue(0x00,0x02)
output = xem.SetWireInValue(0x01,0x00)
output = xem.UpdateWireIns()

xem.ActivateTriggerIn(0x40,0x00)

raw_input("Press enter to continue...")

xem.SetWireInValue(0x00,0x03)
xem.SetWireInValue(0x01,0x01)
xem.UpdateWireIns()

xem.ActivateTriggerIn(0x40,0x00)

raw_input("All LED's should be on, press enter to continue...")

xem.SetWireInValue(0x00,0x03)
xem.SetWireInValue(0x01,0x02)
xem.UpdateWireIns()

xem.ActivateTriggerIn(0x40,0x00)

print('Hello World')
