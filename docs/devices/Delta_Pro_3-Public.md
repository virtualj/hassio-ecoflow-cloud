## Delta_Pro_3

*Sensors*
- Main Battery Level (`bmsBattSoc`)
- Main Design Capacity (`bmsDesignCap`)   _(disabled)_
- Battery Level (`cmsBattSoc`)
- Total In Power (`powInSumW`)
- Total Out Power (`powOutSumW`)
- AC In Power (`powGetAcIn`)
- PV Low-Voltage In Power (`powGetPvH`)
- PV High-Voltage In Power (`powGetPvL`)
- AC High-Voltage Out Power (`powGetAcHvOut`)
- AC Out Power (`powGetAc`)
- Type-C (1) Out Power (`powGetTypec1`)
- Type-C (2) Out Power (`powGetTypec2`)
- DC Car Out Power (`powGet12v`)
- DC Anderson Out Power (`powGet24v`)
- AC Low-Voltage Out Power (`powGetAcLvOut`)
- Alt (1) In Power (`powGet5p8`)
- USB QC (1) Out Power (`powGetQcusb1`)
- USB QC (2) Out Power (`powGetQcusb2`)
- Slave (1) Out Power (`powGet4p81`)
- Slave (2) Out Power (`powGet4p82`)
- AC Low-Voltage TT 30 Out Power (`powGetAcLvTt30Out`)
- Min Cell Temperature (`bmsMinCellTemp`)
- Max Cell Temperature (`bmsMaxCellTemp`)

*Switches*

*Sliders (numbers)*
- AC Charging Power (`cfgPlugInInfoAcInChgPowMax` -> `{"sn": "SN", "cmdId": 17, "dirDest": 1, "dirSrc": 1, "cmdFunc": 254, "dest": 2, "params": {"cfgPlugInInfoAcInChgPowMax": "VALUE"}}` [400 - 2900])
- Max Charge Level (`cfgMaxChgSoc` -> `{"sn": "SN", "cmdId": 17, "dirDest": 1, "dirSrc": 1, "cmdFunc": 254, "dest": 2, "params": {"cfgMaxChgSoc": "VALUE"}}` [50 - 100])
- Min Charge Level (`cfgMinDsgSoc` -> `{"sn": "SN", "cmdId": 17, "dirDest": 1, "dirSrc": 1, "cmdFunc": 254, "dest": 2, "params": {"cfgMinDsgSoc": "VALUE"}}` [0 - 30])
- Backup Reserve Level (`cfgEnergyBackup` -> `{"sn": "SN", "cmdId": 17, "dirDest": 1, "dirSrc": 1, "cmdFunc": 254, "dest": 2, "params": {"cfgEnergyBackup": {"energyBackupStartSoc": value, "energyBackupEn": True}}` [5 - 100])

*Selects*


