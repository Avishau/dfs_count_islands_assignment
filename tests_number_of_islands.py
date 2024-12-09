from number_of_islands import count_islands


def test_number_of_islands():
    grid1 = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert count_islands(grid1) == 0

    grid2 = [
        ["1", "0", "0", "0", "0"],
        ["0", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "1", "0", "0"]
    ]
    assert count_islands(grid2) == 3

    grid3 = [
        ["0", "0", "0", "0", "1"],
        ["0", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["1", "0", "1", "0", "1"]
    ]
    assert count_islands(grid3) == 5

    grid4 = [
        ["1", "0", "0", "1"],
        ["0", "1", "0", "0"],
        ["1", "0", "1", "0"]
    ]
    assert count_islands(grid4) == 5

    grid5 = [[]]
    assert count_islands(grid5) == 0

    # grid6 = [["1" if (i+j) % 2 == 0 else "0" for j in range(300)]
    #          for i in range(300)]
    # assert count_islands(grid6) == 4500

    print("All tests passed successfully!!")

test_number_of_islands()