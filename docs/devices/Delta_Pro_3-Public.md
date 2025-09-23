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
- Min Cell Temperature (`bmsMinCellTemp`)
- Max Cell Temperature (`"bmsMaxCellTemp`)

*Switches*

*Sliders (numbers)*
- AC Charging Power (`cfgPlugInInfoAcInChgPowMax` -> `{"sn": "SN", "cmdId": 17, "dirDest": 1, "dirSrc": 1, "cmdFunc": 254, "dest": 2, "params": {"cfgPlugInInfoAcInChgPowMax": "VALUE"}}` [400 - 2900])
- Max Charge Level (`cfgMaxChgSoc` -> `{"sn": "SN", "cmdId": 17, "dirDest": 1, "dirSrc": 1, "cmdFunc": 254, "dest": 2, "params": {"cfgMaxChgSoc": "VALUE"}}` [50 - 100])
- Min Charge Level (`cfgMinDsgSoc` -> `{"sn": "SN", "cmdId": 17, "dirDest": 1, "dirSrc": 1, "cmdFunc": 254, "dest": 2, "params": {"cfgMinDsgSoc": "VALUE"}}` [0 - 30])
- Backup Reserve Level (`cfgEnergyBackup` -> `{"sn": "SN", "cmdId": 17, "dirDest": 1, "dirSrc": 1, "cmdFunc": 254, "dest": 2, "params": {"cfgEnergyBackup": {"energyBackupStartSoc": value, "energyBackupEn": True}}` [5 - 100])

*Selects*


