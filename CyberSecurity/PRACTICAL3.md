I developed a Python-based forensic application using TestDisk 7.2 and The Sleuth Kit.
It connects to these tools through Python's `subprocess` module.
The application analyzes disk partitions, recovers deleted files, and investigates lost partitions.
For a safe demonstration, I use a dummy 32 MB disk image instead of a physical hard drive.

1. Select **Intel** for the sample disk's MBR partition table.
2. Choose **Proceed**, then **Analyse** to inspect the disk.
3. Run **Quick Search** to find existing or potentially lost partitions.
4. Review the detected partitions and available recovery options.

This application demonstrates disk analysis and recovery with open-source forensic tools.
