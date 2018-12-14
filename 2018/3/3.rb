require 'set'
require 'ostruct'

class DayThree
  def self.claims
    File.readlines('./input').
      map(&:chomp).
      map do |claim|
        regexp = /^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)$/;
        id, left, top, width, height = claim.
          match(regexp).
          captures.
          map(&:to_i)

        OpenStruct.new(
          id: id, 
          left: left, 
          top: top, 
          width: width, 
          height: height
        )
      end
  end

  def self.quilt(grid_size = 1200)
    Array.new(grid_size) do
      Array.new(grid_size) do
        Set.new
      end
    end
  end

  attr_reader :claims, :quilt, :overlaps

  def initialize
    @claims = self.class.claims
    @quilt = self.class.quilt
    @overlaps = Set.new
    populate
  end

  def populate
    claims.each do |claim|
      (claim.top...claim.top + claim.height).each do |y|
        (claim.left...claim.left + claim.width).each do |x|
          quilt[y][x].add(claim.id)
        end
      end
    end
  end

  def part_one
    # How many square inches of fabric are within two or more claims?
    quilt.reduce(0) do |within_many_claims, fabric|
      within_many_claims + fabric.count do |claim_ids|
        claims_for_inch = claim_ids.length
        if claims_for_inch >= 2
          overlaps.merge(claim_ids)
          true
        end
      end
    end
  end

  def part_two
    # What is the ID of the only claim that doesn't overlap?
    claim_without_overlaps = claims.find do |claim|
      !overlaps.include?(claim.id)
    end
    claim_without_overlaps.id
  end

end

day_three = DayThree.new
puts day_three.part_one
puts day_three.part_two