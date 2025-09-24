from ...api import EcoflowApiClient
from ...entities import (
    BaseNumberEntity,
    BaseSelectEntity,
    BaseSensorEntity,
    BaseSwitchEntity,
)
from ...number import (
    ChargingPowerEntity,
    MaxBatteryLevelEntity,
    MinBatteryLevelEntity,
)
from ...sensor import (
    CapacitySensorEntity,
    InWattsSensorEntity,
    LevelSensorEntity,
    OutWattsSensorEntity,
    CelsiusSensorEntity,
)
from .. import BaseDevice, const


class DeltaPro3(BaseDevice):
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [
            LevelSensorEntity(client, self, "bmsBattSoc", const.MAIN_BATTERY_LEVEL).attr("bmsDesignCap", const.ATTR_DESIGN_CAPACITY, 0),
            CapacitySensorEntity(client, self, "bmsDesignCap", const.MAIN_DESIGN_CAPACITY, False),
            LevelSensorEntity(client, self, "cmsBattSoc", const.COMBINED_BATTERY_LEVEL),
            InWattsSensorEntity(client, self, "powInSumW", const.TOTAL_IN_POWER),
            OutWattsSensorEntity(client, self, "powOutSumW", const.TOTAL_OUT_POWER),
            InWattsSensorEntity(client, self, "powGetAcIn", const.AC_IN_POWER),
            InWattsSensorEntity(client, self, "powGetPvH", const.PV_HV_IN_POWER),
            InWattsSensorEntity(client, self, "powGetPvL", const.PV_LV_IN_POWER),
            OutWattsSensorEntity(client, self, "powGetAcHvOut", const.AC_HV_OUT_POWER),
            OutWattsSensorEntity(client, self, "powGetAc", const.AC_OUT_POWER),
            OutWattsSensorEntity(client, self, "powGetTypec1", const.TYPEC_1_OUT_POWER),
            OutWattsSensorEntity(client, self, "powGetTypec2", const.TYPEC_2_OUT_POWER),
            OutWattsSensorEntity(client, self, "powGet12v", const.DC_CAR_OUT_POWER),
            OutWattsSensorEntity(client, self, "powGet24v", const.DC_ANDERSON_OUT_POWER),
            OutWattsSensorEntity(client, self, "powGetAcLvOut", const.AC_LV_OUT_POWER),
            InWattsSensorEntity(client, self, "powGet5p8", const.ALT_1_IN_POWER),
            OutWattsSensorEntity(client, self, "powGetQcusb1", const.USB_QC_1_OUT_POWER),
            OutWattsSensorEntity(client, self, "powGetQcusb2", const.USB_QC_2_OUT_POWER),
            OutWattsSensorEntity(client, self, "powGet4p81", const.SLAVE_N_OUT_POWER % 1),
            OutWattsSensorEntity(client, self, "powGet4p82", const.SLAVE_N_OUT_POWER % 2),
            OutWattsSensorEntity(client, self, "powGetAcLvTt30Out", const.AC_LV_TT30_OUT_POWER),
            CelsiusSensorEntity(client, self, "bmsMinCellTemp", const.MIN_CELL_TEMP),
            CelsiusSensorEntity(client, self, "bmsMaxCellTemp", const.MAX_CELL_TEMP),
            ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return [
            ChargingPowerEntity(
                client,
                self,
                "cfgPlugInInfoAcInChgPowMax",
                const.AC_CHARGING_POWER,
                400,
                2900,
                lambda value: {
                    "sn": self.device_info.sn,
                    "cmdId": 17,
                    "dirDest": 1,
                    "dirSrc": 1,
                    "cmdFunc": 254,
                    "dest": 2,
                    "params": {"cfgPlugInInfoAcInChgPowMax": value},
                },
            ),
            MaxBatteryLevelEntity(
                client,
                self,
                "cfgMaxChgSoc",
                const.MAX_CHARGE_LEVEL,
                50,
                100,
                lambda value: {
                    "sn": self.device_info.sn,
                    "cmdId": 17,
                    "dirDest": 1,
                    "dirSrc": 1,
                    "cmdFunc": 254,
                    "dest": 2,
                    "params": {"cfgMaxChgSoc": value},
                },
            ),
            MinBatteryLevelEntity(
                client,
                self,
                "cfgMinDsgSoc",
                const.MIN_DISCHARGE_LEVEL,
                0,
                30,
                lambda value: {
                    "sn": self.device_info.sn,
                    "cmdId": 17,
                    "dirDest": 1,
                    "dirSrc": 1,
                    "cmdFunc": 254,
                    "dest": 2,
                    "params": {"cfgMinDsgSoc": value},
                },
            ),
            MaxBatteryLevelEntity(
                client,
                self,
                "cfgEnergyBackup",
                const.BACKUP_RESERVE_LEVEL,
                5,
                100,
                lambda value: {
                    "sn": self.device_info.sn,
                    "cmdId": 17,
                    "dirDest": 1,
                    "dirSrc": 1,
                    "cmdFunc": 254,
                    "dest": 2,
                    "params": {"cfgEnergyBackup": {"energyBackupStartSoc": value, "energyBackupEn": True}},
                },
            ),

        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return []

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return []
