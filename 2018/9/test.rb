require_relative "9"

describe "day 9" do
  context "part 1" do
    let(:result) { part1(9, 25) }
    let(:result2) { part1(21, 6111) }
    
    it "finds the winning Elf's score" do
      expect(result).to eq(32)
      expect(result2).to eq(54718)
    end
  end

  context "part 2" do
    let(:result) { part2(447, 71510) }

    it "finds the winning Elf's score with a max multiplier" do
      expect(result).to eq(3273842452)
    end
  end
end

# rspec -fd test.rb