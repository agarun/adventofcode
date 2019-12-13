require_relative "5"

describe "day 5" do
  context "part 1" do
    it "run_computer executes the program" do
      expect(run_computer([3, 0, 4, 0, 99])).to eq([1])
    end

    it "finds the diagnostic code the program produces" do
      expect(part1()).to eq(6069343)
    end
  end

  context "part 2" do
    it "run_computer executes the program" do
      expect(run_computer(
               [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 0
             )).to eq([0])
      expect(run_computer(
               [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 1
             )).to eq([1])
      expect(run_computer(
               [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0
             )).to eq([0])
      expect(run_computer(
               [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 1
             )).to eq([1])
      expect(run_computer(
               [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 7
             )).to eq([999])
      expect(run_computer(
               [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 8
             )).to eq([1000])
      expect(run_computer(
               [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 9
             )).to eq([1001])
    end

    it "finds the diagnostic code the program produces" do
      expect(part2()).to eq(3188550)
    end
  end
end
