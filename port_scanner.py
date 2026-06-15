import socket

target = input("Enter target IP: ")

print(f"\nScanning {target}...\n")

# Open the report file
with open("scan_results.txt", "w") as file:

    file.write(f"Scan Results for {target}\n")
    file.write("=" * 30 + "\n\n")

    for port in range(1, 1025):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:

            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            output = f"[OPEN] {port} ({service})"

            print(output)          # Display on screen
            file.write(output + "\n")  # Save to file

        sock.close()

print("\nScan completed!")
print("Results saved to scan_results.txt")

