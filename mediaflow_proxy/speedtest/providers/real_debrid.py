### replaced URLs with torbox's speedtests ###
from typing import Dict, Tuple, Optional
import random

from mediaflow_proxy.speedtest.models import UserInfo
from mediaflow_proxy.speedtest.providers.base import BaseSpeedTestProvider, SpeedTestProviderConfig


class RealDebridSpeedTest(BaseSpeedTestProvider):
    """Torbox speed test provider implementation."""

    async def get_test_urls(self) -> Tuple[Dict[str, str], Optional[UserInfo]]:
        urls = {
            "EEUR1": "https://storage.torbox.app/100MB.bin",
            "EEUR2": "https://storage.torbox.app/1GB.bin",
            "EEUR3": "https://storage.torbox.app/10GB.bin",
            "WNAM1": "https://hyperdrive.test.wnam.torbox.app/100MB.bin",
            "WNAM2": "https://hyperdrive.test.wnam.torbox.app/1GB.bin",
            "WNAM3": "https://hyperdrive.test.wnam.torbox.app/10GB.bin",
            "APAC1": "https://hyperdrive.test.apac.torbox.app/100MB.bin",
            "APAC2": "https://hyperdrive.test.apac.torbox.app/1GB.bin",
            "APAC3": "https://hyperdrive.test.apac.torbox.app/10GB.bin",
            
        }
        # Add random number to prevent caching
        #urls = {location: f"{base_url}{random.uniform(0, 1):.16f}" for location, base_url in urls.items()}
        return urls, None

    async def get_config(self) -> SpeedTestProviderConfig:
        urls, _ = await self.get_test_urls()
        return SpeedTestProviderConfig(test_duration=10, test_urls=urls)
