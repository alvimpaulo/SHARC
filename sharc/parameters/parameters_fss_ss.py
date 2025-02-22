# -*- coding: utf-8 -*-
from dataclasses import dataclass

from sharc.parameters.parameters_base import ParametersBase

@dataclass
class ParametersFssSs(ParametersBase):
    """Dataclass containing the Fixed Satellite Services - Space Station
    parameters for the simulator
    """
    section_name: str = "FSS_SS"
    # satellite center frequency [MHz]
    frequency: float = 43000.0
    # satellite bandwidth [MHz]
    bandwidth: float = 200.0
    # Peak transmit power spectral density (clear sky) [dBW/Hz]
    tx_power_density: float = -5.0
    # satellite altitude [m]
    altitude: float = 35780000.0
    # satellite latitude [deg]
    lat_deg: float = 0.0
    # Elevation angle [deg]
    elevation: float = 270.0
    # Azimuth angle [deg]
    azimuth: float = 0.0
    # System receive noise temperature [K]
    noise_temperature: float = 950.0
    # Adjacent channel selectivity (dB)
    adjacent_ch_selectivity: float = 0.0
    # Satellite peak receive antenna gain [dBi]
    antenna_gain: float = 46.6
    # Antenna pattern of the FSS space station
    # Possible values: "ITU-R S.672", "ITU-R S.1528", "FSS_SS", "OMNI"
    antenna_pattern: str = "FSS_SS"
    # IMT parameters relevant to the satellite system
    #    altitude of IMT system (in meters)
    #    latitude of IMT system (in degrees)
    #    difference between longitudes of IMT and satellite system
    #      (positive if space-station is to the East of earth-station)
    imt_altitude: float = 0.0
    imt_lat_deg: float = 0.0
    imt_long_diff_deg: float = 0.0
    # Season of the year used by the channel model.
    season: str = "SUMMER"
    # Channel parameters
    # channel model, possible values are "FSPL" (free-space path loss),
    #                                    "SatelliteSimple" (FSPL + 4 + clutter loss)
    #                                    "P619"
    channel_model: str = "P619"
    # The required near-in-side-lobe level (dB) relative to peak gain
    # according to ITU-R S.672-4
    antenna_l_s: float = -20.0
    # 3 dB beamwidth angle (3 dB below maximum gain) [degrees]
    antenna_3_dB: float = 0.65

    def load_parameters_from_file(self, config_file: str):
        """Load the parameters from file an run a sanity check

        Parameters
        ----------
        file_name : str
            the path to the configuration file

        Raises
        ------
        ValueError
            if a parameter is not valid
        """
        super().load_parameters_from_file(config_file)

        # Now do the sanity check for some parameters
        if self.antenna_pattern not in ["ITU-R S.672", "ITU-R S.1528", "FSS_SS", "OMNI"]:
            raise ValueError(f"ParametersFssSs: \
                             invalid value for parameter antenna_pattern - {self.antenna_pattern}. \
                             Possible values \
                             are \"ITU-R S.672\", \"ITU-R S.1528\", \"FSS_SS\", \"OMNI\"")

        if self.season.upper() not in ["SUMMER", "WINTER"]:
            raise ValueError(f"ParametersFssSs: \
                             Invalid value for parameter season - {self.season}. \
                             Possible values are \"SUMMER\", \"WINTER\".")

        if self.channel_model.upper() not in ["FSPL", "SatelliteSimple", "P619"]:
            raise ValueError(f"ParametersFssSs: \
                             Invalid value for paramter channel_model = {self.channel_model}. \
                             Possible values are \"FSPL\", \"SatelliteSimple\", \"P619\".")
