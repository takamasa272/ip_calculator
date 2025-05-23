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

    if ip.version == 4:
        if ip.network.prefixlen <= 30:
            print("\nNetwork   : " + str(ip.network[0]))
            print("Min host  : " + str(ip.network[1]))
            print("Max host  : " + str(ip.network[-2]))
            print("Broadcast : " + str(ip.network[-1]))
        
        elif ip.network.prefixlen == 31:
            print("\nNetwork   : " + str(ip.network[0]))
            print("Broadcast : " + str(ip.network[-1]))

    # There is no Broadcast address in IPv6
    if ip.version == 6:
        if ip.network.prefixlen <= 64:
            print("\nNetwork   : " + str(ip.network[0]))
            print("Min host  : " + str(ip.network[1]))
            print("Max host  : " + str(ip.network[-129]))
            print("Max range : " + str(ip.network[-1]))
        
        elif ip.network.prefixlen <= 126:
            print("\nNetwork   : " + str(ip.network[0]))
            print("Min host  : " + str(ip.network[1]))
            print("Max range : " + str(ip.network[-1]))

        elif ip.network.prefixlen == 127:
            print("\nNetwork   : " + str(ip.network[0]))
            print("Max range : " + str(ip.network[-1]))

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
    print("Number of hosts: " + str(calc_numhost(ip)))
    print("Integer : " + str(int(ip.ip)))
    print("PTR record: " + str(ip.ip.reverse_pointer))

    print("\n")


def calc_numhost(ip) -> int:
    if ip.version == 4:
        if ip.network.prefixlen <= 30:
            return 2 ** (32 - ip.network.prefixlen) - 2
        else:
            return 2 ** (32 - ip.network.prefixlen)
    else:
        if ip.network.prefixlen <= 64:
            return 2 ** (128 - ip.network.prefixlen) - 128
        elif ip.network.prefixlen <= 126:
            return 2 ** (128 - ip.network.prefixlen) - 1
        else:
            return 2 ** (128 - ip.network.prefixlen)


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
