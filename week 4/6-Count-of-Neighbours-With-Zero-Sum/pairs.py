def count_zero_neighbours(numbers):

    count = 0
    index = 0

    for number in numbers:
        if index < len(numbers)- 1:
            neighbour = numbers[index + 1]

            if neighbour + number == 0:
                count += 1
        index += 1

    return count


