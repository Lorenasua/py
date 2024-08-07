public static void noseque(){}
    int solution(String directions) {
        int x = 0, y = 0; // Initial position of the robot
        int direction = 0; // 0: North, 1: East, 2: South, 3: West
        
        // Iterate through each character in the directions string
        for (char c : directions.toCharArray()) {
            // Handle turning right
            if (c == 'R') {
                // Turn the robot 90 degrees to the right
                direction = (direction + 1) % 4;
            } 
            // Handle turning left
            else if (c == 'L') {
                // Turn the robot 90 degrees to the left
                direction = (direction + 3) % 4; // Equivalent to (direction - 1 + 4) % 4
            } 
            // Handle moving forward
            else if (c == 'F') {
                // Move the robot forward one step based on the current direction
                if (direction == 0) y++;
                else if (direction == 1) x++;
                else if (direction == 2) y--;
                else x--;
            }
        }
        
        // Calculate the Manhattan distance from the starting point (0, 0)
        int distance = Math.abs(x) + Math.abs(y);
        
        // Return the minimum number of commands needed to return to the starting point
        return distance;
    
    
}
