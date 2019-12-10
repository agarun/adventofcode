ADD = 1
MULTIPLY = 2
STOP = 99

def run_computer(intcode_program)
  (0...intcode_program.length).step(4) do |index|
    opcode = intcode_program[index]
    case opcode
    when ADD
      sum_idx_1 = intcode_program[index + 1]
      sum_idx_2 = intcode_program[index + 2]
      storage_idx = intcode_program[index + 3]
      sum = intcode_program[sum_idx_1] + intcode_program[sum_idx_2]
      intcode_program[storage_idx] = sum
    when MULTIPLY
      product_idx_1 = intcode_program[index + 1]
      product_idx_2 = intcode_program[index + 2]
      storage_idx = intcode_program[index + 3]
      product = intcode_program[product_idx_1] * intcode_program[product_idx_2]
      intcode_program[storage_idx] = product
    when STOP
      return intcode_program
    else
      raise "this is not an opcode"
    end
  end

  intcode_program
end

def part1(noun = 12, verb = 2)
  intcode_program = File.read("./input").split(",").map(&:to_i)
  intcode_program[1] = noun
  intcode_program[2] = verb
  run_computer(intcode_program)[0]
end

def part2(target_output)
  intcode_program = File.read("./input").split(",").map(&:to_i)
  (0..99).each do |noun|
    (0..99).each do |verb|
      output = part1(noun, verb)
      return 100 * noun + verb if output == target_output
    end
  end
end