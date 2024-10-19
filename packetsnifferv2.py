import pyshark
from datetime import datetime

# List to store packet captures
packet_captures = []

def packet_callback(packet):
    try:
        # Get the current time
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Extract protocol type, source IP, and destination IP
        protocol = packet.highest_layer
        source_ip = packet.ip.src
        destination_ip = packet.ip.dst
        
        # Determine if the packet is receiving or sending based on the destination IP
        direction = "Receiving" if destination_ip == SPECIFIC_IP else "Sending"
        
        # Store the packet capture in the list with time
        packet_captures.append(f"{timestamp} | {direction:<10} | {protocol:<10} | {source_ip:<15} | {destination_ip}")

    except AttributeError:
        # Skip packets that do not have the required attributes
        pass

def main():
    global SPECIFIC_IP, INTERFACE  # Make SPECIFIC_IP and INTERFACE accessible within main
    
    # Prompt the user for their IP address
    SPECIFIC_IP = input("Please enter the specific IP address of the host: ")

    # Prompt the user for the interface they want to use
    print("Select the interface you want to use:")
    print("1. Wi-Fi")
    print("2. Loopback")
    print("3. Ethernet")
    print("4. Bluetooth")
    interface_choice = input("Enter the number of your choice: ")

    # Set the interface based on user input
    if interface_choice == "1":
        INTERFACE = "Wi-Fi"
    elif interface_choice == "2":
        INTERFACE = "Adapter for loopback traffic capture"
    elif interface_choice == "3":
        INTERFACE = "Ethernet 2"
    elif interface_choice == "4":
        INTERFACE = "Bluetooth Network Connection"
    else:
        print("Invalid choice. Defaulting to Wi-Fi.")
        INTERFACE = "Wi-Fi"

    # Get the current date and time
    start_time = datetime.now().strftime("%H:%M:%S")
    
    # Open the file in write mode to clear any previous session data
    with open('capturedpackets.txt', 'w') as f:
        f.write(f"Packet capture session started at: {start_time}\n\n")
        # Write table header
        f.write(f"{'Time':<8} | {'Direction':<10} | {'Protocol':<10} | {'Source IP':<15} | {'Destination IP'}\n")
        f.write('-' * 75 + '\n')  # Underline the header

    # Start capturing packets
    capture = pyshark.LiveCapture(interface=INTERFACE)
    
    print("Starting packet capture. Press Ctrl+C to stop.")
    
    try:
        capture.apply_on_packets(packet_callback)
    except KeyboardInterrupt:
        print("Packet capture stopped.")
        
        # Write all captured packets to the text file at the end of the session
        with open('capturedpackets.txt', 'a') as f:
            f.write("\n".join(packet_captures))  # Append the list of captures

if __name__ == "__main__":
    main()
