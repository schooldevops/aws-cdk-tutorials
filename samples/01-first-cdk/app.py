#!/usr/bin/env python3
import os

import aws_cdk as cdk

from 01_first_cdk.01_first_cdk_stack import FirstCdkStack


app = cdk.App()
FirstCdkStack(app, "01FirstCdkStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.
    
    # 만약 'evn'를 지정하지 않는다면 이 스택은 환경을 무시할 것이다. 
    # Account/Region-dependent 기능들과 컨텍스트 룩업은 동작하지 않을 것이다. 
    # 그러나 단일 합성된 템플릿은 어디든지 배포될 수 있다.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    # 현재 CLI 구성에 의해서 암시하는 AWS 계정 및 Region 에 대해 이 스택을 특수화 하려면 다음 주석을 해제하라.
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */
    
    # 만약 정확히 어떠한 계정과 리젼으로 스택을 배포하기를 원한다면 다음 주석을 해제하라.
    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
