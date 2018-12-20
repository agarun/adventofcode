class Marble
  attr_reader :value
  attr_accessor :prev, :next

  def initialize(value)
    @value = value
    @prev = self
    @next = self
  end

  def remove
    curr_prev = self.prev
    curr_next = self.next

    curr_prev.next = curr_next
    curr_next.prev = curr_prev

    self
  end
end

class Player
  attr_accessor :score, :num
  
  def initialize(num)
    @num = num
    @score = 0
  end
end

class Circle
  def insert_marble_between(marble, first, second)
    first.next = marble
    second.prev = marble

    marble.next = second
    marble.prev = first
  end

  def find(starting_marble, distance, direction = -1)
    if direction == -1
      # counter-clockwise
      target_marble = starting_marble
      distance.times do
        target_marble = target_marble.prev
      end
    end

    target_marble
  end

  def remove_marble(marble)
    marble.remove
  end
end

class Game
  attr_accessor :current_player, :current_marble, :lowest_remaining_value
  attr_reader :circle, :max_points, :players

  def initialize(num_players, max_points, options = {})
    @players = Array.new(num_players) { |num| Player.new(num) }
    @max_points = max_points * options.fetch(:multiplier, 1)
    @current_player = @players[0]
    @circle = Circle.new
    @current_marble = Marble.new(0)
    @lowest_remaining_value = 1
  end

  def play
    until lowest_remaining_value > max_points
      turn
    end
  end

  def next_player
    i = current_player.num
    self.current_player = players[(i + 1) % players.length]
  end

  def turn
    marble = Marble.new(lowest_remaining_value)

    if lowest_remaining_value % 23 == 0
      current_player.score += marble.value
      seven_marbles_away = circle.find(current_marble, 7)
      removed_marble = circle.remove_marble(seven_marbles_away)
      current_player.score += seven_marbles_away.value

      self.current_marble = seven_marbles_away.next
    else
      one_away = self.current_marble.next
      two_away = self.current_marble.next.next
      
      circle.insert_marble_between(marble, one_away, two_away)

      self.current_marble = marble
    end

    self.lowest_remaining_value += 1
    next_player    
  end

  def winner
    players.max { |p1, p2| p1.score <=> p2.score }.score
  end
end

def part1(num_players, max_points)
  game = Game.new(num_players, max_points)
  game.play
  game.winner
end

def part2(num_players, max_points)
  game = Game.new(num_players, max_points, multiplier: 100)
  game.play
  game.winner
end

if __FILE__ == $PROGRAM_NAME
  input = File.readlines("./input").
    map(&:chomp)

  input.each do |game|
    regexp = /^(\d+)\D+(\d+).+/;
    num_players, max_points = game.
      match(regexp).
      captures.
      map(&:to_i)

    puts part1(num_players, max_points)
    puts part2(num_players, max_points)
  end
end
