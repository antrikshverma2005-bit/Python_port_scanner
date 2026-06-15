import socket

target = input("Enter target IP: ")

print(f"\nScanning {target}...\n")

with open("scan_results.txt", "w") as report:

    report.write(f"Scan Results for {target}\n")
    report.write("=" * 50 + "\n\n")

    for port in range(1, 1025):

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:

                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"

                output = f"[OPEN] Port {port} ({service})"

                print(output)
                report.write(output + "\n")

                # Banner Grabbing
                try:
                    banner_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    banner_sock.settimeout(2)

                    banner_sock.connect((target, port))

                    banner = banner_sock.recv(1024).decode(
                        errors="ignore"
                    ).strip()

                    if banner:
                        banner_output = f"Banner: {banner}"
                    else:
                        banner_output = "Banner: Not Available"

                except:
                    banner_output = "Banner: Not Available"

                print(banner_output)
                report.write(banner_output + "\n\n")

                try:
                    banner_sock.close()
                except:
                    pass

            sock.close()

        except:
            pass

print("\nScan completed.")
print("Results saved to scan_results.txt")