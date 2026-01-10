"""Azure AI Services integration module"""

import json
from typing import Dict, Any, List, Optional


class AzureIntegrationHelper:
    """Helper class for Azure AI Services integration."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Azure integration helper.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        
    def get_azure_openai_config_template(self) -> Dict[str, Any]:
        """Get Azure OpenAI configuration template.
        
        Returns:
            Configuration template
        """
        return {
            "endpoint": "https://YOUR-RESOURCE-NAME.openai.azure.com/",
            "api_key": "YOUR-API-KEY",
            "api_version": "2024-02-01",
            "deployment_name": "gpt-4",  # or gpt-4-turbo, gpt-4o, gpt-4.1
            "temperature": 0.7,
            "max_tokens": 800,
            "top_p": 0.95,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
    
    def get_ai_search_config_template(self) -> Dict[str, Any]:
        """Get Azure AI Search configuration template.
        
        Returns:
            Configuration template
        """
        return {
            "endpoint": "https://YOUR-SEARCH-SERVICE.search.windows.net",
            "api_key": "YOUR-ADMIN-KEY",
            "index_name": "your-index",
            "semantic_configuration": "default",
            "query_type": "semantic",
            "top": 5
        }
    
    def interactive_mode(self):
        """Run in interactive mode for Azure integration."""
        print("\n☁️  Azure AI Services Integration Mode\n")
        
        print("Azure AI Services enhance your M365 agents with:")
        print("  • Azure OpenAI - GPT-4, GPT-4.1, GPT-5 models")
        print("  • Azure AI Search - Intelligent search with RAG")
        print("  • Azure Cognitive Services - Speech, Vision, Language")
        print("  • Azure Machine Learning - Custom model deployment")
        print("  • Azure AI Studio - End-to-end AI development\n")
        
        print("🤖 Azure OpenAI Service:")
        print("   Available Models (2025):")
        print("   • GPT-4 - Advanced reasoning and creativity")
        print("   • GPT-4 Turbo - Faster, cost-effective")
        print("   • GPT-4o - Multimodal (text, image, audio)")
        print("   • GPT-4.1 - Latest model with improved quality")
        print("   • GPT-5 family - Preview access available")
        print("   • o1 series - Advanced reasoning models")
        
        print("\n🔍 Azure AI Search (RAG):")
        print("   • Vector search for semantic similarity")
        print("   • Hybrid search (keyword + vector)")
        print("   • Semantic ranking")
        print("   • Integration with OpenAI embeddings")
        print("   • Support for 512MB documents")
        
        print("\n🧠 Integration Patterns:")
        print()
        print("1. RAG (Retrieval-Augmented Generation)")
        print("   • Index your enterprise data in AI Search")
        print("   • User queries trigger semantic search")
        print("   • Relevant docs retrieved and sent to GPT")
        print("   • GPT generates answer grounded in your data")
        
        print("\n2. Custom Engine Copilot")
        print("   • Build agent in Copilot Studio")
        print("   • Connect to Azure OpenAI deployment")
        print("   • Fine-tune system prompts")
        print("   • Control temperature, tokens, behavior")
        
        print("\n3. Multi-Modal Agents")
        print("   • Process images with GPT-4o")
        print("   • Generate speech with Azure Speech")
        print("   • Analyze documents with Document Intelligence")
        print("   • Create rich, visual responses")
        
        print("\n💰 Cost Considerations:")
        print("   • Pay per token (input + output)")
        print("   • GPT-4 Turbo more cost-effective than GPT-4")
        print("   • AI Search: Pay per index size and queries")
        print("   • Free tiers available for development/testing")
        
        print("\n🔒 Security & Compliance:")
        print("   • Enterprise-grade security")
        print("   • Data residency options")
        print("   • Private endpoints")
        print("   • Microsoft Purview integration")
        print("   • GDPR, HIPAA, SOC 2 compliant")
        
        print("\n💡 Quick Start:")
        print("  1. Create Azure OpenAI resource in Azure Portal")
        print("  2. Deploy a model (e.g., gpt-4, gpt-4-turbo)")
        print("  3. Get API key and endpoint")
        print("  4. (Optional) Create AI Search service")
        print("  5. Index your data in AI Search")
        print("  6. Connect to Copilot Studio or custom agent")
        print("  7. Test with your enterprise data")
        
        print("\n📚 Resources:")
        print("  • Azure OpenAI: https://learn.microsoft.com/en-us/azure/ai-services/openai/")
        print("  • Azure AI Search: https://learn.microsoft.com/en-us/azure/search/")
        print("  • RAG Pattern: https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview")
        print("  • Integration guide: docs/integration-recommendations.md")
        
        print("\n📋 Configuration Templates:")
        print("\nAzure OpenAI:")
        print(json.dumps(self.get_azure_openai_config_template(), indent=2))
        print("\nAzure AI Search:")
        print(json.dumps(self.get_ai_search_config_template(), indent=2))
        
        input("\nPress Enter to return to main menu...")
