ADD = 1
MULTIPLY = 2
STOP = 99
SAVE = 3
PUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8

PARAMETER_MODE = 0
IMMEDIATE_MODE = 1

def parameter_modes(parameter)
  ones = parameter % 10
  tens = parameter / 10 % 10
  hundreds = parameter / 100 % 10
  [ones, tens, hundreds]
end

def value(position, program, mode)
  if mode == PARAMETER_MODE
    program[program[position]]
  elsif mode == IMMEDIATE_MODE
    program[position]
  end
end

def run_computer(intcode_program, input = 1)
  outputs = []
  index = 0

  while index < intcode_program.length
    opcode = intcode_program[index] % 100 # rightmost 2 digits
    parameter_instruction = (intcode_program[index] - opcode) / 100 # everything but rightmost 2 digits
    modes = parameter_modes(parameter_instruction)

    case opcode
    when ADD
      parameter_1 = value(index + 1, intcode_program, modes[0])
      parameter_2 = value(index + 2, intcode_program, modes[1])
      parameter_3 = value(index + 3, intcode_program, IMMEDIATE_MODE)
      intcode_program[parameter_3] = parameter_1 + parameter_2

      index += 4
    when MULTIPLY
      parameter_1 = value(index + 1, intcode_program, modes[0])
      parameter_2 = value(index + 2, intcode_program, modes[1])
      parameter_3 = value(index + 3, intcode_program, IMMEDIATE_MODE)
      intcode_program[parameter_3] = parameter_1 * parameter_2

      index += 4
    when SAVE
      parameter_1 = value(index + 1, intcode_program, IMMEDIATE_MODE)
      intcode_program[parameter_1] = input

      index += 2
    when PUT
      output = value(index + 1, intcode_program, modes[0])
      outputs << output

      index += 2
    when JUMP_IF_TRUE
      parameter_1 = value(index + 1, intcode_program, modes[0])
      parameter_2 = value(index + 2, intcode_program, modes[1])

      index = parameter_1.nonzero? ? parameter_2 : index + 3
    when JUMP_IF_FALSE
      parameter_1 = value(index + 1, intcode_program, modes[0])
      parameter_2 = value(index + 2, intcode_program, modes[1])

      index = parameter_1.zero? ? parameter_2 : index + 3
    when LESS_THAN
      parameter_1 = value(index + 1, intcode_program, modes[0])
      parameter_2 = value(index + 2, intcode_program, modes[1])
      parameter_3 = value(index + 3, intcode_program, IMMEDIATE_MODE)
      intcode_program[parameter_3] = parameter_1 < parameter_2 ? 1 : 0

      index += 4
    when EQUALS
      parameter_1 = value(index + 1, intcode_program, modes[0])
      parameter_2 = value(index + 2, intcode_program, modes[1])
      parameter_3 = value(index + 3, intcode_program, IMMEDIATE_MODE)
      intcode_program[parameter_3] = parameter_1 == parameter_2 ? 1 : 0

      index += 4
    when STOP
      break
    else
      raise "this is not an opcode"
    end
  end

  outputs
end

def intcode_program
  File.read("./input").split(",").map(&:to_i)
end

def diagnostic_code(outputs)
  non_zero_outputs = outputs.count(&:nonzero?)
  if non_zero_outputs == 1
    outputs.find { |output| !output.zero? }
  end
end

def part1()
  diagnostic_code(run_computer(intcode_program, 1))
end

def part2()
  diagnostic_code(run_computer(intcode_program, 5))
end
