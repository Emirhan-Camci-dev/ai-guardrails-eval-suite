with open("redguard-community/src/lib.rs", "r") as f:
    content = f.read()

# Remove the bad patch if it's there at the top
if content.startswith("impl Default for GuardrailEngine"):
    content = content.split("}\n}\n", 1)[1]

import re
replacement = """
impl Default for GuardrailEngine {
    fn default() -> Self {
        Self::new()
    }
}

impl GuardrailEngine {
"""
content = content.replace("impl GuardrailEngine {", replacement)

with open("redguard-community/src/lib.rs", "w") as f:
    f.write(content)
