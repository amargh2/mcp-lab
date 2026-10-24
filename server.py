import socket
import ipaddress
from mcp.server import MCPServer

# 1. Initialize the MCP server with a human-readable name
mcp = MCPServer("SysAdmin Tools")

# 2. Define our tool
@mcp.tool()
def resolve_dns(domain: str) -> str:
    """Resolve a domain name (e.g., 'google.com') to its IPv4 address."""
    try:
        ip = socket.gethostbyname(domain)
        return f"{domain} resolves to {ip}"
    except socket.gaierror as err:
        return f"DNS lookup failed for {domain}: {err}"

# 3. Additional tool - test tool
@mcp.tool()
def get_hostname() -> str:
    """Get the hostname of the current machine I am using. 
       What is this computer called?"""
    try:
        hostname = socket.gethostname()
        return f"The hostname of this machine is {hostname}"
    except Exception as err:
        return f"Failed to get hostname: {err}"

@mcp.tool()
def calculate_subnet(network: str) -> str:
    """Calculate complete subnet details for an IPv4 CIDR block (e.g. '192.168.0.0/16')."""
    try:
        net = ipaddress.ip_network(network, strict=False)

        # Handle special edge cases (/31 point-to-point and /32 single host)
        if net.prefixlen == 32:
            usable_hosts = 1
            host_range = f"{net.network_address}"
        elif net.prefixlen == 31:
            usable_hosts = 2
            host_range = f"{net.network_address} to {net.broadcast_address}"
        else:
            usable_hosts = net.num_addresses - 2
            host_range = f"{net.network_address + 1} to {net.broadcast_address - 1}"

        return (
            f"Subnet Profile for {network}:\n"
            f"• Netmask: {net.netmask}\n"
            f"• Wildcard Mask: {net.hostmask}\n"
            f"• Network Address: {net.network_address}\n"
            f"• Broadcast Address: {net.broadcast_address}\n"
            f"• Usable Host Count: {usable_hosts:,}\n"
            f"• Usable Range: {host_range}\n"
            f"• Scope: {'Private (RFC 1918)' if net.is_private else 'Public Internet'}"
        )
    except Exception as err:
        return f"Invalid network '{network}': {err}"    
# 3. Standard entry point: runs stdio transport by default
if __name__ == "__main__":
    mcp.run()