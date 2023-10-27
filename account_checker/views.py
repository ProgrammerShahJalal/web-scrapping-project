from django.shortcuts import render
from .models import LinkedInAccount


def home(request):
    return render(request, 'index.html')

def check_account_status(request):
    """Checks the status of LinkedIn accounts.

    Args:
        request: A Django HttpRequest object.

    Returns:
        A Django HttpResponse object.
    """

    # Get the URLs of the LinkedIn profiles from the request.
    profile_urls = request.GET.getlist("https://www.linkedin.com/in/ProgrammerShahJalal/")

    # Create a list of LinkedInAccount objects.
    linkedin_accounts = []
    for profile_url in profile_urls:
        linkedin_account = LinkedInAccount(profile_url=profile_url)
        linkedin_account.status = check_linkedin_account_status(profile_url)
        linkedin_accounts.append(linkedin_account)

    # Save the LinkedInAccount objects to the database.
    LinkedInAccount.objects.bulk_create(linkedin_accounts)

    # Render the template with the list of LinkedInAccount objects.
    return render(request, "account_checker/check_account_status.html", {"linkedin_accounts": linkedin_accounts})

