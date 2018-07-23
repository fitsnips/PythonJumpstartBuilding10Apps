#!/usr/bin/env python3
import movie_svc
import requests.exceptions


def main():
    banner()
    search_event_loop()


def banner():
    print('------------------------------------------------------')
    print('                 Movie Search App                     ')
    print('------------------------------------------------------')
    print()

def search_event_loop():
    search = "ONCE_THROUGH_LOOP"
    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ').rstrip().lower()
            if search != 'x':
                results = movie_svc.find_movies(search)
                for r in results:
                    print('{} -- {}'.format(
                        r.year, r.title
                    ))
                print()
        except ValueError:
            print('Error: search text is required')
        except requests.exceptions.ConnectionError:
            print('Error: Please check network connection.')
        except Exception as x:
            print('Error: unable to run search at this time!')
            # to see type of exception
            #print('Details: {}'.format(type(x)))
            print('Details: {}'.format(x))


    print('Exiting .....')


if __name__ == '__main__':
    main()
