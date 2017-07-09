class InvalidCommandException(Exception):
    def out_log(self):
        print("コマンド不正")
