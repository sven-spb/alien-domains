import asyncio
import ipaddress
import aiodns
from dotenv import dotenv_values


async def check_domain_records_async(domains: list[str], subnet: str, target_ns: list[str]) -> None:
    resolver = aiodns.DNSResolver()
    subnet = ipaddress.ip_network(subnet)
    target_ns = [ns.lower() for ns in target_ns]

    async def check_domain(domain) -> None:
        try:
            ns_records = await resolver.query(domain, 'NS')
            ns_values = [ns.host.lower() for ns in ns_records]
            if any(ns in ns_values for ns in target_ns):
                return
            a_records = await resolver.query(domain, 'A')
            for a_record in a_records:
                ip = ipaddress.ip_address(a_record.host)
                if ip in subnet:
                    print(f"Domain: {domain}, A Record: {a_record.host}")
        except (aiodns.error.DNSError, asyncio.TimeoutError):
            pass

    await asyncio.gather(*(check_domain(domain) for domain in domains))

async def main() -> None:
    SUBNET = config["SUBNET"]
    TARGET_NS = [ns.strip() for ns in config.get("TARGET_NS", "").split(",")]
    domains = ["domain1.tld", "domain2.tld"]
    await check_domain_records_async(domains, SUBNET, TARGET_NS)

if __name__ == "__main__":
    config = dotenv_values()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print()
