import time

# Read fragments from the file
with open("source.txt", "r") as file:
    fragments = [line.strip() for line in file]

def find_best_sequence(fragments):
    """
    This function finds the longest sequence by connecting fragments based on matching last two digits
    of one fragment and the first two digits of the next one.
    """
    # Store possible connections
    connections = {fragment: [] for fragment in fragments}

    # Check possible connections between fragments
    for frag1 in fragments:
        for frag2 in fragments:
            if frag1 != frag2 and frag1[-2:] == frag2[:2]:  # Check if last two digits of frag1 match first two digits of frag2
                connections[frag1].append(frag2)

    # Function to find the longest chain recursively
    def build_sequence(start, visited):
        """
        Recursively builds the longest sequence starting from a given fragment, ensuring no fragment is reused.
        """
        sequence = start  # Start with the current fragment
        visited.add(start)  # Mark the current fragment as visited
        next_fragments = connections[start]  # Get the possible next fragments

        if not next_fragments:
            return sequence  # Return the sequence if there are no more fragments to add

        longest = ""  # Initialize variable for the longest sequence
        for next_frag in next_fragments:
            if next_frag not in visited:
                result = build_sequence(next_frag, visited.copy())  # Recursive call for the next fragment
                if len(result) > len(longest):  # Update the longest sequence if needed
                    longest = result

        return sequence + longest[2:]  # Add the longest sequence without the first two digits (already part of the current fragment)

    best_sequence = ""
    for frag in fragments:
        sequence = build_sequence(frag, set())  # Start the search from each fragment
        if len(sequence) > len(best_sequence):  # Update the best sequence if a longer one is found
            best_sequence = sequence

    return best_sequence

if __name__ == "__main__":
    # Measure execution time
    start_time = time.time()
    result = find_best_sequence(fragments)
    end_time = time.time()

    # Calculate elapsed time in minutes and seconds
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)

    # Print the result and the time taken
    print(result)
    print(f"time: {minutes} min {seconds} sec")

