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

binary_easement_tree = {
  "question": "Is there a dominant and servient tenement?",
  "yes": {
    "question": "Are the dominant and servient tenements owned by different persons?",
    "yes": {
      "question": "Does the right claimed accommodate the dominant tenement?",
      "yes": {
        "question": "Is the right claimed capable of forming the subject matter of a grant?",
        "yes": {
          "question": "Is the right sufficiently defined?",
          "yes": {
            "question": "Does the right impose a positive burden on the servient tenement?",
            "no": {
              "question": "Does the right oust the servient owner from reasonable use of their land?",
              "no": {
                "question": "Is the right being used for the benefit of the dominant tenement only?",
                "yes": {
                  "question": "Was the easement created by express grant or reservation?",
                  "yes": {
                    "question": "Does it meet the formalities to create at law (deed and registration)?",
                    "yes": "Easement created by express grant or reservation",
                    "no": "Equitable easement created by express grant or reservation"
                  },
                  "no": {
                    "question": "Was the easement created by implied grant or reservation?",
                    "yes": {
                      "question": "Was the easement created by necessity?",
                      "yes": "Easement created by necessity",
                      "no": {
                        "question": "Was the easement created by intended use?",
                        "yes": "Easement created by intended use",
                        "no": "No easement"
                      }
                    },
                    "no": {
                      "question": "Was the easement created by prescription?",
                      "yes": {
                        "question": "Has the right been used for 20 years?",
                        "yes": {
                          "question": "Was the use 'as of right' (nec vi, nec clam, nec precario)?",
                          "yes": "Easement created by prescription",
                          "no": "No easement"
                        },
                        "no": "No easement"
                      },
                      "no": "No easement"
                    }
                  }
                },
                "no": "No easement due to benefit to non-dominant land"
              },
              "yes": "No easement due to ouster principle"
            },
            "yes": "No easement due to positive burden on servient tenement"
          },
          "no": "No easement due to insufficiently defined right"
        },
        "no": "No easement due to incapability of forming the subject matter of a grant"
      },
      "no": "No easement due to lack of accommodation of the dominant tenement"
    },
    "no": "No easement due to same ownership of dominant and servient tenements"
  },
  "no": "No easement due to lack of dominant and servient tenement"
}


binary_adv_poss_tree = {
  "question": "Is the land registered?",
  "yes": {
    "question": "Has the squatter been in possession for at least 10 years?",
    "yes": {
      "question": "Is the land adjacent to land already owned by the squatter?",
      "yes": {
        "question": "Has the squatter reasonably believed for 10 years that the land belonged to them?",
        "yes": {
          "question": "Did the squatter's belief in ownership remain reasonable until shortly before the application?",
          "yes": "A case for adverse possession can be made out.",
          "no": "A case for adverse possession cannot be made out."
        },
        "no": "A case for adverse possession cannot be made out."
      },
      "no": {
        "question": "Can the squatter establish an equity by estoppel making it unconscionable for the registered proprietor to dispossess the squatter?",
        "yes": "A case for adverse possession can be made out.",
        "no": {
          "question": "Is the squatter entitled to be the registered proprietor for some other reason?",
          "yes": "A case for adverse possession can be made out.",
          "no": "A case for adverse possession cannot be made out."
        }
      }
    },
    "no": "A case for adverse possession cannot be made out."
  },
  "no": {
    "question": "Has the squatter been in possession for at least 12 years?",
    "yes": {
      "question": "Has the owner discontinued possession or been dispossessed?",
      "yes": {
        "question": "Has the squatter had exclusive factual possession and intention to possess?",
        "yes": {
          "question": "Has the squatter possessed the land without the owner's consent?",
          "yes": "A case for adverse possession can be made out.",
          "no": "A case for adverse possession cannot be made out."
        },
        "no": "A case for adverse possession cannot be made out."
      },
      "no": "A case for adverse possession cannot be made out."
    },
    "no": "A case for adverse possession cannot be made out."
  }
}

binary_priv_nuis_tree = {
  "question": "Is there a consequential, indirect interference with the claimant's land?",
  "yes": {
    "question": "Does the interference fall into one of these categories: encroachment, direct physical injury, or interference with comfort and convenience?",
    "yes": {
      "question": "Is there an unreasonable interference?",
      "yes": {
        "question": "Does the interference cause more than de minimis damage?",
        "yes": {
          "question": "Does the interference relate to a protected right (e.g., bad smells, smoke, excessive noise)?",
          "yes": {
            "question": "Is the interference reasonably foreseeable?",
            "yes": {
              "question": "Is the claimant hypersensitive or using the land in a way that increases susceptibility to the interference?",
              "yes": {
                "question": "Would the interference affect normal use of the land?",
                "yes": "Claim for private nuisance can be made.",
                "no": "Claim for private nuisance cannot be made."
              },
              "no": "Claim for private nuisance can be made."
            },
            "no": "Claim for private nuisance cannot be made."
          },
          "no": "Claim for private nuisance cannot be made."
        },
        "no": "Claim for private nuisance cannot be made."
      },
      "no": "Claim for private nuisance cannot be made."
    },
    "no": "Claim for private nuisance cannot be made."
  },
  "no": "Claim for private nuisance cannot be made."
}



all_trees = {
    1: {
        "tree_name": "Easement",
        "tree": binary_easement_tree
    },
    2: {
        "tree_name": "Adverse Possession",
        "tree": binary_adv_poss_tree
    },
    3: {
        "tree_name": "Private Nuisance",
        "tree": binary_priv_nuis_tree
    }
}

tree_names = [
    {"id": 1, "name": "Easement"},
    {"id": 2, "name": "Adverse Possession"},
    {"id": 3, "name": "Private Nuisance"}
]
