import setuptools

setuptools.setup(
    name='timecode_tools',
    description="Scripts for generating LTC wave files ahead of time and MTC MIDI events in realtime.",
    long_description=open('README.md').read(),

    author='jeffmikels',

    python_requires='>=3.7',
    packages=setuptools.find_packages(),
    install_requires=[
        "timecode",
        "mido",
        "python-rtmidi",
        "click",
    ],
    )
