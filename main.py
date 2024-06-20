from web.web_init_driver import init_driver


def main():
    try:
        # Starting Process
        print("The process has started.")

        init_driver()

    except Exception as e:
        print(f'An error occurred in Orchestrator Module:\n[{e}]')

    finally:
        # End Process
        print("The process has finished.")


if __name__ == '__main__':
    main()
