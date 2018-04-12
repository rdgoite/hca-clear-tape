# Clear Tape

This is a tool that compiles together all the metadata from a given HCA bundle 
into a single JSON. Bundle contents are added as objects to one big JSON array.

## Usage

This utility currently only supports generation of JSON for one bundle at a 
time. To the script takes a bundle UUID as a command line argument:

    python clear-tape.py <bundle_uuid>
    
The script prints the results to the standard output, which can then be 
directed to a file:

    python clear-tape.py <bundle_uuid> > /path/to/file.json
    
### Data Store API

By default, the script connects to `https://dss.dev.data.humancellatlas.org/v1`
to find the bundles. However, it can be configured to query a different 
instance of the DSS by setting the `CT_DSS_API` environment variable before
the script is run:

    $ export CT_DSS_API=https://dss.data.humancellatlas.org/v1
    $ python clear-tape.py <bundle_uuid>
    
The sample execution above will set the script to query the production DSS.

## Assumptions

The current version of this tool assumes that all inputs are correct and 
verified (externally). There is very limited hand testing done on the script 
that checks that it works for very simple, expected cases (happy path). 
There is little to no error handling in the current code, and so it may 
behave in unexpected ways given bad inputs. As the operations do not involve
state changing requests, there should be little risk when things go awry. It
is assumed that the DSS is secure enough to guard or recover from anything
unexpected brought about by running this tool.
