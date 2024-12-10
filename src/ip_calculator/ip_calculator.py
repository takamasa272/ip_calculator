import sys
import ipaddress


def main():
    if len(sys.argv) <= 1:
        ip = ipaddress.ip_interface(input("input ip >>> "))
    else:
        ip = ipaddress.ip_interface(sys.argv[1])

    print("\n[ADDRESS]")
    print("IP address : " + str(ip.ip))
    print("Netmask    : " + str(ip.netmask))
    print("Hostmask   : " + str(ip.hostmask))
    print("NW prefix  : " + str(ip.network))

    if (
        ip.version == 4
        and ip.network.prefixlen <= 30
        or ip.version == 6
        and ip.network.prefixlen <= 126
    ):
        print("\nNetwork   : " + str(ip.network[0]))
        print("Min host  : " + str(ip.network[1]))
        print("Max host  : " + str(ip.network[-2]))
        print("Broadcast : " + str(ip.network[-1]))
    elif (
        ip.version == 4
        and ip.network.prefixlen == 31
        or ip.version == 6
        and ip.network.prefixlen == 127
    ):
        print("\nNetwork   : " + str(ip.network[0]))
        print("Broadcast : " + str(ip.network[-1]))

    print("\n[BINARY]")
    print("IP address : " + to_bin(ip.ip))
    print("Netmask    : " + to_bin(ip.netmask))
    print("Hostmask   : " + to_bin(ip.hostmask))
    print("NW prefix  : " + to_bin(ip.network[0]))

    print("\n[FLAGS]")
    if ip.is_private:
        print("Private address")
    if ip.is_global:
        print("Global address")
    if ip.is_link_local:
        print("Link local address")
    if ip.is_loopback:
        print("Loopback address")
    if ip.is_multicast:
        print("Multicast address")
    if ip.is_unspecified:
        print("Unspecified address")
    if ip.is_reserved:
        print("Reserved address")

    print("\n[Supplement]")
    print("Integer : " + str(int(ip.ip)))
    print("PTR record: " + str(ip.ip.reverse_pointer))

    print("\n")


# convert IP address to binary
def to_bin(ip) -> str:
    if ip.version == 4:
        return ".".join([format(int(octet), "08b") for octet in str(ip).split(".")])

    elif ip.version == 6:
        dont_omit_ip = "{:_n}".format(ip)  # 一度、_区切りにしてしまう
        return ":".join(
            [format(int(octet, 16), "016b") for octet in dont_omit_ip.split("_")]
        )
    else:
        raise ValueError("Invalid IP address")


if __name__ == "__main__":
    main()
