require_relative "2"

describe "day 2" do
  context "part 1" do
    it "run_computer executes the program" do
      expect(run_computer([1,9,10,3,2,3,11,0,99,30,40,50])).to eq([3500,9,10,70,2,3,11,0,99,30,40,50])
      expect(run_computer([1,0,0,0,99])).to eq([2,0,0,0,99])
      expect(run_computer([2,3,0,3,99])).to eq([2,3,0,6,99])
      expect(run_computer([2,4,4,5,99,0])).to eq([2,4,4,5,99,9801])
      expect(run_computer([1,1,1,4,99,5,6,0,99])).to eq([30,1,1,4,2,5,6,0,99])
    end

    it "finds the value at position 0 after modifications" do
      expect(part1()).to eq(3931283)
    end
  end

  context "part 2" do
    it "finds the input noun and verb that cause the program to product correct output" do
      expect(part2(19690720)).to eq(6979)
    end
  end
end