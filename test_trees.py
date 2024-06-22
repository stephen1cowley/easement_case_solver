easement_tree = {
"question": "Is there a dominant and servient tenement?",
"yes": {
"question": "Are the dominant and servient tenements owned by different persons?",
"yes": {
    "question": "Does the right claimed accommodate the dominant tenement?",
    "yes": {
    "question": "Is the right claimed capable of forming the subject matter of a grant?",
    "yes": {
        "question": "Is the easement being used for the benefit of the dominant tenement only?",
        "yes": {
        "question": "Does the right impose a positive burden on the servient tenement?",
        "no": {
            "question": "Is the right sufficiently defined?",
            "yes": {
            "question": "Does the right oust the servient owner from reasonable use of their land?",
            "no": {
                "question": "How was the easement created?",
                "Express grant/reservation": {
                    "question": "Does it meet the formalities to create at law?",
                    "yes": "Easement created by express grant/reservation",
                    "no": "Easement created by equitable means"
                },
                "Implied grant/reservation": {
                    "question": "Was the land subdivided?",
                    "yes": {
                    "question": "Is it an easement of necessity or intended use?",
                    "Easement of necessity": "Easement created by necessity",
                    "Easement of intended use": "Easement created by intended use"

                    },
                    "no": "No easement"
                },
                "Prescription": {
                    "question": "Has the right been used for 20 years?",
                    "yes": {
                    "question": "Was the use 'as of right' (nec vi, nec clam, nec precario)?",
                    "yes": "Easement created by prescription",
                    "no": "No easement"
                    },
                    "no": "No easement"
                }
            },
            "yes": "No easement due to ouster principle"
            },
            "no": "No easement due to insufficiently defined right"
        },
        "yes": "No easement due to positive burden on servient tenement"
        },
        "no": "No easement due to benefit to non-dominant land"
    },
    "no": "No easement due to incapability of forming the subject matter of a grant"
    },
    "no": "No easement due to lack of accommodation of the dominant tenement"
},
"no": "No easement due to same ownership of dominant and servient tenements"
},
"no": "No easement due to lack of dominant and servient tenement"
}
