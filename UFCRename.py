from nzbget import PostProcessScript

class UFCRename(PostProcessScript):
    """Inheriting PostProcessScript grants you access to of the API defined
       throughout this wiki
    """

    def main(self, *args, **kwargs):
        """Use validation when you've defined more then one option
        """
        if not self.validate(keys=(
            'Debug',
            'MyOptionA',
            'MyOptionB')):
            # Fail if your options aren't found
            return False

        if not self.health_check()
            # Content was never unpacked, there is nothing to Post-Process
            # but there is also no reason to fail (return False) since
            # there isn't anything we can do anyway.
            return None

        # Write your code here knowing all of your options are correctly
        # set in memory
        
        files = self.get_files(
           self.directory,
           suffix_filter='.mkv,.avi,.divx,.xvid,.mov,.wmv,.mp4,.mpg,.mpeg,.vob,.iso'
        )

        print files