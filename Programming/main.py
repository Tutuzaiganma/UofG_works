if __name__ == "__main__":
    def flatten_list(nested_list):
    
        for item in list:
            if isinstance(item, list):
                flatten_list(item)
            else:
                print(item)
    data = input("Enter a nested list (e.g., [1, [2, 3], 4]): ")
    flatten_list( data )

                

