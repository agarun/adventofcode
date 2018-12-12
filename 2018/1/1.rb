# 1
puts File.open('./input', 'r').map(&:to_i).reduce(:+)

# 2
current_frequency = 0
frequencies_reached = Hash.new(0) # or frequencies_seen = Set.new()

loop do
  File.foreach('./input') do |line|
    num = line.to_i
    current_frequency += num
    frequencies_reached[current_frequency] += 1

    if frequencies_reached[current_frequency] == 2
      puts current_frequency
      return
    end
  end
end