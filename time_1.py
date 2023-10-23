class time:
    """The time class stores general information about a time.
    """

    def __init__(self, hour: int, minute: int, second: int):
        """Constructs a time object having the specified hour, minute, and second,
        and universal time in the format HH:MM:SS.

        :ivar __hour: hour of this time object
        :ivar __minute: minute of this time object
        :ivar __second: second of this time object
        :ivar __time: universal time of this time object in the format HH:MM:SS

        Args:
            hour (int): specified hour
            minute (int): specified minute
            second (int): specified second

        Raises:
            ValueError: indicates specified hour is less than 0 or greater than 24
            ValueError: indicates specified minute is less than 0 or greater than 60
            ValueError: indicates specified second is less than 0 or greater than 60
        """

        time = (hour, minute, second)

        try:
            if (hour < 0 or hour >= 24):
                raise ValueError("Hour is less than zero or greater than 23.")
            if (minute < 0 or minute >= 60):
                raise ValueError("Minute is less than zero or greater than 59")
            if (second < 0 or second >= 60):
                raise ValueError("Second is less than zero or greater than 59")
        except ValueError as e:
            exit(e)
        else:
            self.__hour = hour
            self.__minute = minute
            self.__second = second
            time = f"{self.__hour}:{self.__minute}:{self.__second}"
            self.__time = time


        

    def getHour(self):
        """Returns the hour of the calling time object.\
        
        Returns:
            int: hour of the calling time object
        """
        return self.__hour

    def setHour(self, hour: int):
        """Sets the hour of the calling time object to the specified hour and
        recomputes the universal time of the calling time object.

        Args:
            hour (int): specified hour

        Raises:
            ValueError: indicates specified hour is less than 0 or greater than 24
        """

        try:
            if self.__hour < 0 or self.__hour >= 24:
                raise ValueError("Hour is less than zero or greater than 23")
        except ValueError as e:
            exit(e)
        else:
            self.__hour = hour
            

    def getMinute(self):
        """Returns the minute of the calling time object.

        Returns:
            int: minute of the calling time object
        """
        return self.__minute

    def setMinute(self, minute: int):
        """Sets the minute of the calling time object to the specified minute and
        recomputes the universal time of the calling time object.

        Args:
            minute (int): specified minute

        Raises:
            ValueError: indicates specified minute is less than 0 or greater than 60
        """
        try:
            if self.__minute < 0 or self.__minute >= 60:
                raise ValueError("Minute is less than zero or greater than 59")
        except ValueError as e:
            exit(e)
        else:
            self.__minute = minute

    def getSecond(self):
        """Returns the second of the calling time object.

        Returns:
            int: second of the calling time object
        """
        return self.__second

    def setSecond(self, second: int):
        """Sets the second of the calling time object to the specified second and
        recomputes the universal time of the calling time object.

        Args:
            second (int): specified second
    
        Raises:
            ValueError: indicates specified second is less than 0 or greater than 60
        """

        try:
            if self.__second < 0 or self.__second >= 60:
                raise ValueError("Second is less than zero or greater than 59")
        except ValueError as e:
            exit(e)
        else:
            self.__second = second        


    def getTime(self):
        """Returns the universal time of the calling time object.

        Returns:
            str: universal time of the calling time object
        """
        return self.__time

    def __str__(self):
        """Returns string representation of the calling time object.

        Returns:
            str: string representation of the calling time object
        """
        return f"{self.__hour}:{self.__minute}:{self.__second}"


    def __eq__(self, other):
        """Tests if the calling time object is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling time object is equal to the specified
            object, else False
        """
        if other is not None:
            # check if other is an account type
            if isinstance(other, time):
                # check if other's balance is equal to the balance
                # of the calling object
                if (other.__hour == self.__hour) and (other.__minute == self.__minute) and (other.__second == self.__second):
                    return True
                
        return False        

    @staticmethod
    def sort(data, first: int, last: int):
        """Sorts a list from smallest to largest using the insertion sort
        algorithm bypassing the elements to the left of first and to the
        right of last.

        Args:
            data: list to sort
            first (int): list index at which the sort will begin
            last (int): list index at which the sort will end
        """
    # initialize loop counter variable i to 1
        i = 1

        #initialize loop counter variable j to 0
        j = 0

        # initialize next value to 0
        nextVal = 0

        # loop through list as many times as speciified by the 
        # length of the list and first
        # this loop represents the blue arrow in the slides
        while(i < len(data) - first):
            # store a copy of a number in index position first + i 
            # in next value
            nextVal = data[first+i]

            # loop through the list starting at the same index as
            # next value and iterate back toward first as long as 
            # the element to the left of next value is greater than
            # next value and we're not the whole way back to first
            j = first + i
            while(j > first and data[j-1] > nextVal):
                # shift the element to the left of the next value right
                # ward one position
                data[j] = data[j - 1]

                # insert next value into the element that was just
                # shifted
                data[j-1] = nextVal

                # decrement j by 1
                j = j-1

            # increment i by 1
            i = i + 1
    @staticmethod
    def search (a, first: int, last: int, target: int):
        """Searches part of a sorted list for a specified target starting at a[first]
        and ending at a[last].

        Args:
            a (int): the list to search
            first (int): the list index at which the search will start
            last (int): the list index at which the search will end
            target (int): the element to search for
        Returns:
            int: If target appears in the list, index of the, element
            that contains target; else -1.
        """

        # set an int variable i to 0
        i = 0

        # set a boolean variable found to false
        found = False

        # while there are more elements to search
        # and the target hasn't been found
        # i plus first doesn't exceed i + first
        while ((i < len(a)) and not found and (i + first < last)):
            # if the current element is the target
            if (a[i + first] == target):
                # set found to true
                found = True
            else:
                # incremement i by 1
                i += 1
            
        # check if the target was found
        if (found):
            #return index of target
            return i + first
        else:
            # return negative 1
            return -1