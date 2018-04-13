# Clear Tape

This is a tool that compiles together all the metadata from a given HCA bundle 
into a single JSON. Bundle contents are added as objects to one big JSON array.

## Dependencies

Clear Tape is developed as a Python 3 application. All the depencies needed
to run and/or develop this tool is listed in the `requirements.txt` file,
which can be used as input to the `pip` utility:

    pip install -r requirements.txt

## Usage

### Configuration

By default, the script is set to run against development environment, 
connecting to Ingest Core in `http://api.ingest.dev.data.humancellatlas.org` 
and DSS in `https://dss.dev.data.humancellatlas.org/v1` to find and process 
the bundles. However, it can be configured to use a different deployment 
environment by setting the `CT_ENV` environment variable before the script 
is run. As the time of writing, there are only 2 options available: `DEV` 
for the development environment, and `PROD`, for the production environment.

    export CT_ENV=PROD
    
The sample execution above will set the script to query the production 
servers.

### Running the Script

This utility takes in a submission id and outputs compilation of all the
bundles that have been generated from the given submission:

    python clear_tape.py <bundle_uuid>
    
Running the command above will create files in the `output` directory of
the present working directory. All files are by default prefixed with the
name `bundle` and are numbered based on the order they are process. For
example, a submission that generates 3 bundles will have files 
`bundle_1.json`, `bundle_2.json`, and `bundle_3.json` in the `output` 
directory. The prefix can be set to something else by setting a second
argument to the script:

    python clear_tape.py <bundle_uuid> my_bundle
    
The command above will create `my_bundle_*.json` in the `output` directory.
Changing the prefix is useful when generating compilations from different
bundles, setting each to use their own unique prefix.
   

## Assumptions

The current version of this tool assumes that all inputs are correct and 
verified (externally). There is very limited hand testing done on the script 
that checks that it works for very simple, expected cases (happy path). 
There is little to no error handling in the current code, and so it may 
behave in unexpected ways given bad inputs. As the operations do not involve
state changing requests, there should be little risk when things go awry. It
is assumed that the DSS is secure enough to guard or recover from anything
unexpected brought about by running this tool.
